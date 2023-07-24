let displayValue = '';
let firstValue = '';
let secondValue = '';
let operation = '';
let prevAnswer = '';


function addToDisplay(value) {
    if (value == '+' || value == '-' || value == '*' || value == '/') {
        operation = value;

        switch (operation) {
            case '/':
                document.getElementById("divide-operator").style.backgroundColor = 'white';
                document.getElementById("minus-operator").style.backgroundColor = 'orange';
                document.getElementById("multiply-operator").style.backgroundColor = 'orange';
                document.getElementById("plus-operator").style.backgroundColor = 'orange';
                document.getElementById("divide-operator").style.color = 'orange';
                document.getElementById("minus-operator").style.color = 'white';
                document.getElementById("multiply-operator").style.color = 'white';
                document.getElementById("plus-operator").style.color = 'white';
                break;
            case '-':
                document.getElementById("divide-operator").style.backgroundColor = 'orange';
                document.getElementById("minus-operator").style.backgroundColor = 'white';
                document.getElementById("multiply-operator").style.backgroundColor = 'orange';
                document.getElementById("plus-operator").style.backgroundColor = 'orange';
                document.getElementById("divide-operator").style.color = 'white';
                document.getElementById("minus-operator").style.color = 'orange';
                document.getElementById("multiply-operator").style.color = 'white';
                document.getElementById("plus-operator").style.color = 'white';
                break;
            case '*':
                document.getElementById("divide-operator").style.backgroundColor = 'orange';
                document.getElementById("minus-operator").style.backgroundColor = 'orange';
                document.getElementById("multiply-operator").style.backgroundColor = 'white';
                document.getElementById("plus-operator").style.backgroundColor = 'orange';
                document.getElementById("divide-operator").style.color = 'white';
                document.getElementById("minus-operator").style.color = 'white';
                document.getElementById("multiply-operator").style.color = 'orange';
                document.getElementById("plus-operator").style.color = 'white';
                break;
            case '+':
                document.getElementById("divide-operator").style.backgroundColor = 'orange';
                document.getElementById("minus-operator").style.backgroundColor = 'orange';
                document.getElementById("multiply-operator").style.backgroundColor = 'orange';
                document.getElementById("plus-operator").style.backgroundColor = 'white';
                document.getElementById("divide-operator").style.color = 'white';
                document.getElementById("minus-operator").style.color = 'white';
                document.getElementById("multiply-operator").style.color = 'white';
                document.getElementById("plus-operator").style.color = 'orange';
                break;
            default:
                break;
        }

    } else {
        if (operation == '') {
            firstValue += value;
            displayValue = firstValue;
        } else {
            secondValue += value;
            displayValue = secondValue;
        }
        document.getElementById("display").value = displayValue;
    }
}

function clearOperationColor() {
    document.getElementById("divide-operator").style.backgroundColor = 'orange';
    document.getElementById("minus-operator").style.backgroundColor = 'orange';
    document.getElementById("multiply-operator").style.backgroundColor = 'orange';
    document.getElementById("plus-operator").style.backgroundColor = 'orange';
    document.getElementById("divide-operator").style.color = 'white';
    document.getElementById("minus-operator").style.color = 'white';
    document.getElementById("multiply-operator").style.color = 'white';
    document.getElementById("plus-operator").style.color = 'white';
}

function clearAll() {
    displayValue = '0';
    firstValue = '';
    secondValue = '';
    operation = '';
    clearOperationColor();
    document.getElementById("display").value = displayValue;
}

function calculate() {
    try {
        const result = eval(firstValue + operation + secondValue);
        displayValue = result.toString();
        prevAnswer = result.toString();
        firstValue = displayValue;
        secondValue = '';
        operation = '';
        clearOperationColor();
        document.getElementById("display").value = displayValue;
    } catch (error) {
        displayValue = "Error";
        document.getElementById("display").value = displayValue;
    }
}

function prevAnswerFunc() {
    displayValue += prevAnswer
    document.getElementById("display").value = displayValue;
}

function plusMinusOperation() {
    if (secondValue == '') {
        firstValue = Number(firstValue) * -1;
        displayValue = firstValue.toString();
    } else {
        secondValue = Number(secondValue) * -1;
        displayValue = secondValue.toString();
    }
    document.getElementById("display").value = displayValue;
}

function flashElement(element) {
    let prevColor = element.style.backgroundColor
    element.style.backgroundColor = 'white';
    setTimeout(() => {
        element.style.backgroundColor = prevColor;
        }, 150
    )
}
