from py_rules.components import Condition, Result, Rule
from py_rules.engine import RuleEngine

def Hib(Patient):
    condition = Condition('age', '>', 6) & Condition('age', '<', 59)
    # Create a condition

    doNotAdminister = ["Asplenia" , "hyposplenism" , "Cancer" , "HIV"  , "Hemoglobinopathies" , "HIV" ]


    # Create a result
    result = Result('message', 'str', 'Eligible for vaccine!')

    rule = Rule('Hib').If(condition).Then(result)

    # initialise a new instance of RuleEngine with context
    context = {'age': Patient["age"]}

    engine = RuleEngine(context)

    return (engine.evaluate(rule))
    # Eligible for vaccine!

def PolioEligibility(Patient):
    condition = Condition('age', '>', 48) & Condition('age', '<', 84)
    # Create a condition

    doNotAdminister = ["Asplenia" , "hyposplenism" , "Cancer" , "HIV"  , "Hemoglobinopathies" , "HIV" ]


    # Create a result
    result = Result('message', 'str', 'Eligible for vaccine!')

    rule = Rule('Polio').If(condition).Then(result)

    # initialise a new instance of RuleEngine with context
    context = {'age': Patient["age"]}

    engine = RuleEngine(context)

    return (engine.evaluate(rule))
    # Eligible for vaccine!

def PolioEligibility(Patient):
    condition = Condition('age', '>', 48) & Condition('age', '<', 84)
    # Create a condition

    doNotAdminister = ["Asplenia" , "hyposplenism" , "Cancer" , "HIV"  , "Hemoglobinopathies" , "HIV" ]


    # Create a result
    result = Result('message', 'str', 'Eligible for vaccine!')

    rule = Rule('Polio').If(condition).Then(result)

    # initialise a new instance of RuleEngine with context
    context = {'age': Patient["age"]}

    engine = RuleEngine(context)

    return (engine.evaluate(rule))
    # Eligible for vaccine!

def Rotavirus(Patient):
    FirstDoseCondition = Condition('age', '>', 1.3) & Condition('age', '<', 3.5)
    SecondDoseCondition = Condition()
    # Create a condition

    doNotAdminister = ["Asplenia" , "hyposplenism" , "Cancer" , "HIV"  , "Hemoglobinopathies" , "HIV" ]


    # Create a result
    result = Result('message', 'str', 'Eligible for vaccine!')

    rule = Rule('Polio').If(condition).Then(result)

    # initialise a new instance of RuleEngine with context
    context = {'age': Patient["age"]}

    engine = RuleEngine(context)

    return (engine.evaluate(rule))
    # Eligible for vaccine!