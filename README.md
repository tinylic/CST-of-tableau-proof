## requirements
Python 2.7

## Usage

The input propositions are stored in **input.txt**

```bash
    python solveformula.py input.txt
```

Python solveformula.py InputFileName


### Example

#### Input1 :

(A\_{1} \and A\_{2}) \imply (A\_{3} \iff B)


#### Output1 :

F ((A\_{1} \and A\_{2}) \imply (A\_{3} \iff B))

F ((A\_{1} \and A\_{2}) \imply (A_{3} \iff B))

T (A\_{1} \and A\_{2})

F (A\_{3} \iff B)

T A\_{1}

T A\_{2}

T B

F A\_{3}

Counterexample:  B A\_{1} A\_{2}

#### Input2 :

(B \or \not B)

#### Output2 :

F (B \or \not B)

F (B \or \not B)

F B

F \not B

T B

It is tableau provable.