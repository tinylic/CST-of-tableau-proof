import re
from CST import Atom

def Proposition_Filter(InputProp) :
    InputProp = re.sub('[\{\}]', '', InputProp)
    InputProp = re.sub('\\\\not', '~', InputProp)#not
    InputProp = re.sub('\\\\and', '&', InputProp)#and
    InputProp = re.sub('\\\\or', '|', InputProp)#or
    InputProp = re.sub('\\\\imply', '>>', InputProp)#imply
    InputProp = re.sub('\\\\iff', '<<', InputProp)#iff
    return InputProp

def dop(f):
    print("Formula: ", f)
    CounterExample = f.proof()
    if (CounterExample is None) :
        print "It is tableau provable."
        return
    else :
        print "Counterexample: ",
        for variable in CounterExample :
            print variable,

def solve(InputProp) :
    print InputProp
    Prop = Proposition_Filter(InputProp)

    variables = re.findall(r'[AB]_[0-9]+', Prop)
    variables += ['A', 'B']
    for variable in variables :
        exec(variable + ' = Atom(\'' + variable + '\')')

    dop(eval(Prop))
