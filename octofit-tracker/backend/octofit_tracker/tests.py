from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", email="testuser@example.com", password="password123")

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="teamuser", email="teamuser@example.com", password="password123")
        Team.objects.create(name="Test Team", members=[user])

    def test_team_creation(self):
        team = Team.objects.get(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="activityuser", email="activityuser@example.com", password="password123")
        Activity.objects.create(user=user, activity_type="Running", duration="01:00:00")

    def test_activity_creation(self):
        activity = Activity.objects.get(activity_type="Running")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="leaderboarduser", email="leaderboarduser@example.com", password="password123")
        Leaderboard.objects.create(user=user, score=100)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.get(score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutTestCase(TestCase):
    def setUp(self):
        Workout.objects.create(name="Test Workout", description="This is a test workout.")

    def test_workout_creation(self):
        workout = Workout.objects.get(name="Test Workout")
        self.assertEqual(workout.name, "Test Workout")
