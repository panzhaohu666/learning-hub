from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pw-alice-123')

    def test_user_field_is_required(self):
        # 断言必须是 IntegrityError，不能写成 Exception：后者会把测试自身的
        # 笔误、导入错误、拼错字段名一律算作通过。
        with self.assertRaises(IntegrityError):
            Task.objects.create(title='没有归属的任务')

    def test_str_returns_title(self):
        task = Task.objects.create(user=self.user, title='买牛奶')
        self.assertEqual(str(task), '买牛奶')

    def test_default_ordering_is_newest_first(self):
        first = Task.objects.create(user=self.user, title='第一条')
        second = Task.objects.create(user=self.user, title='第二条')
        self.assertEqual(list(Task.objects.all()), [second, first])

    def test_deleting_user_cascades_to_tasks(self):
        Task.objects.create(user=self.user, title='会被级联删除')
        self.user.delete()
        self.assertEqual(Task.objects.count(), 0)


class TaskListTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username='alice', password='pw-alice-123')
        self.bob = User.objects.create_user(username='bob', password='pw-bob-123')

    def test_anonymous_is_redirected_to_login(self):
        response = self.client.get(reverse('task_list'))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('task_list'))

    def test_only_own_tasks_are_listed(self):
        Task.objects.create(user=self.alice, title='alice 的任务')
        Task.objects.create(user=self.bob, title='bob 的任务')
        self.client.login(username='alice', password='pw-alice-123')
        response = self.client.get(reverse('task_list'))
        self.assertContains(response, 'alice 的任务')
        self.assertNotContains(response, 'bob 的任务')

    def test_counts_only_cover_own_tasks(self):
        Task.objects.create(user=self.alice, title='a1', completed=True)
        Task.objects.create(user=self.alice, title='a2')
        Task.objects.create(user=self.bob, title='b1', completed=True)
        self.client.login(username='alice', password='pw-alice-123')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.context['total_count'], 2)
        self.assertEqual(response.context['completed_count'], 1)


class TaskCreateTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pw-alice-123')

    def test_create_assigns_current_user(self):
        self.client.login(username='alice', password='pw-alice-123')
        self.client.post(reverse('task_create'), {'title': '新任务', 'description': '说明'})
        task = Task.objects.get(title='新任务')
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.description, '说明')

    def test_blank_title_creates_nothing(self):
        self.client.login(username='alice', password='pw-alice-123')
        self.client.post(reverse('task_create'), {'title': '   '})
        self.assertEqual(Task.objects.count(), 0)

    def test_anonymous_post_creates_nothing(self):
        self.client.post(reverse('task_create'), {'title': '匿名的任务'})
        self.assertEqual(Task.objects.count(), 0)


class TaskMutationTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username='alice', password='pw-alice-123')
        self.bob = User.objects.create_user(username='bob', password='pw-bob-123')
        self.alice_task = Task.objects.create(user=self.alice, title='alice 的任务')
        self.bob_task = Task.objects.create(user=self.bob, title='bob 的任务')

    def test_toggle_flips_completed(self):
        self.client.login(username='alice', password='pw-alice-123')
        self.client.post(reverse('task_toggle', args=[self.alice_task.pk]))
        self.alice_task.refresh_from_db()
        self.assertTrue(self.alice_task.completed)

    def test_toggle_on_foreign_task_returns_404(self):
        self.client.login(username='alice', password='pw-alice-123')
        response = self.client.post(reverse('task_toggle', args=[self.bob_task.pk]))
        self.assertEqual(response.status_code, 404)
        self.bob_task.refresh_from_db()
        self.assertFalse(self.bob_task.completed)

    def test_delete_on_foreign_task_returns_404(self):
        self.client.login(username='alice', password='pw-alice-123')
        response = self.client.post(reverse('task_delete', args=[self.bob_task.pk]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Task.objects.filter(pk=self.bob_task.pk).exists())

    def test_delete_removes_own_task(self):
        self.client.login(username='alice', password='pw-alice-123')
        self.client.post(reverse('task_delete', args=[self.alice_task.pk]))
        self.assertFalse(Task.objects.filter(pk=self.alice_task.pk).exists())

    def test_clear_completed_only_touches_own_tasks(self):
        Task.objects.create(user=self.alice, title='a-done', completed=True)
        Task.objects.create(user=self.bob, title='b-done', completed=True)
        self.client.login(username='alice', password='pw-alice-123')
        self.client.post(reverse('task_clear_completed'))
        self.assertFalse(Task.objects.filter(user=self.alice, completed=True).exists())
        self.assertTrue(Task.objects.filter(user=self.bob, completed=True).exists())

    def test_get_is_rejected_for_state_changing_views(self):
        self.client.login(username='alice', password='pw-alice-123')
        for name, args in (
            ('task_toggle', [self.alice_task.pk]),
            ('task_delete', [self.alice_task.pk]),
            ('task_clear_completed', []),
        ):
            response = self.client.get(reverse(name, args=args))
            self.assertEqual(response.status_code, 405, msg=name)
        self.alice_task.refresh_from_db()
        self.assertFalse(self.alice_task.completed)
        self.assertTrue(Task.objects.filter(pk=self.alice_task.pk).exists())


class AuthViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pw-alice-123')

    def test_logout_rejects_get(self):
        self.client.login(username='alice', password='pw-alice-123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(self.client.get(reverse('task_list')).status_code, 200)

    def test_logout_via_post_ends_session(self):
        self.client.login(username='alice', password='pw-alice-123')
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 302)

    def test_register_creates_user_and_logs_in(self):
        response = self.client.post(
            reverse('register'),
            {'username': 'newuser', 'password1': 'complex-pw-987', 'password2': 'complex-pw-987'},
        )
        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertEqual(self.client.get(reverse('task_list')).status_code, 200)

    def test_login_with_wrong_password_stays_on_page(self):
        response = self.client.post(reverse('login'), {'username': 'alice', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get(reverse('task_list')).status_code, 302)

    def test_login_with_correct_password_redirects(self):
        response = self.client.post(reverse('login'), {'username': 'alice', 'password': 'pw-alice-123'})
        self.assertRedirects(response, reverse('task_list'))

    def test_login_missing_username_returns_page_not_500(self):
        # request.POST['username'] 缺字段会抛 KeyError → 500。表单被裁剪、
        # 用户禁用 JS 或被中间件改写时都可能真的发出这种请求。
        response = self.client.post(reverse('login'), {'password': 'pw-alice-123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '用户名和密码不能为空')

    def test_login_with_next_redirects_to_next(self):
        # next 必须指向一个「默认跳转不会去」的地址，否则旧代码无条件
        # redirect('task_list') 也能让这条通过，测不出 next 有没有生效。
        target = reverse('register')
        self.assertNotEqual(target, reverse('task_list'))
        response = self.client.post(
            reverse('login'),
            {'username': 'alice', 'password': 'pw-alice-123', 'next': target},
        )
        self.assertRedirects(response, target)

    def test_login_next_rejects_external_host(self):
        # 开放重定向：next 指向外部站点时必须落回默认页，不能照着跳。
        response = self.client.post(
            reverse('login'),
            {'username': 'alice', 'password': 'pw-alice-123', 'next': 'https://evil.example/steal'},
        )
        self.assertRedirects(response, reverse('task_list'))

    def test_login_form_carries_next_into_hidden_field(self):
        target = reverse('register')
        response = self.client.get(reverse('login'), {'next': target})
        self.assertContains(response, 'name="next"')
        self.assertContains(response, f'value="{target}"')
