#------------------------------------------------------------------------
#loosely created classes that I might use later in other parts of the app
#------------------------------------------------------------------------
from functions import current_date

class Users():
	def __init__(self, first_name, second_name, user_id):
		self.first_name = first_name
		self.second_name = second_name
		self.user_id = user_id

class Goals():
	def __init__(self, objective, deadline, goal_type):
		self.objective = objective
		self.deadline = deadline
		self.goal_type = goal_type
		self.achieved = "Undergoing"
	
	def goal_achieved(self):
		self.achieved = "Finished"

	def goal_failed(self):
		self.achieved = "Failed"

	def change_deadline(self, new_deadline):
		self.deadline = new_deadline


class Habits():
	def __init__(self, habit, habit_type):
		self.habit = habit
		self.habit_type = habit_type

class Stats():
	def __init__(self, stat, stat_type):
		self.stat = stat
		self.stat_type = stat_type

class Consumables():
	def __init__(self, consumable, consumable_type):
		self.consumable = consumable
		self.consumable_type = consumable_type

class Daily_stats():
	def __init__(self, weight, steps, kcals):
		self.weight = weight
		self.steps = steps
		self.kcals = kcals
		self.date = current_date()


