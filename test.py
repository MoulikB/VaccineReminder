from py_rules.components import Condition, Result, Rule
from py_rules.engine import RuleEngine

# Create a condition
condition = Condition('temperature', '>=', 40) | Condition('wind_speed', '>', 50)

# Create a result
result = Result('message', 'str', 'Unfavourable weather conditions for work!')

# Create a rule
rule = Rule('Temperature Rule').If(condition).Then(result)

# initialise a new instance of RuleEngine with context
context = {'temperature': 45, 'wind_speed': 30}
engine = RuleEngine(context)

print(engine.evaluate(rule))
# 'Unfavourable weather conditions for work!'

# if a Rule is used without a Result, it simply returns True/False
rule = Rule('Bool Temperature Rule').If(condition)
print(engine.evaluate(rule))
# True