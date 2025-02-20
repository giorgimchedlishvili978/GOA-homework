<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .calculator {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        input[type="number"] {
            width: 100px;
            padding: 8px;
            margin: 10px 0;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 15px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="calculator">
      </h2>
        <input type="number" id="num1" placeholder
        <input type="number" id="num2" placeholder
        <br>
        <button onclick="calculate('+')"(+)</button>
        <button onclick="calculate('-')"> (-)</button>
        <div class="result" id="result"></div>
    </div>

    <script>
        function calculate(operation) {
            //
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            
            // 
            let result;
            if (operation === '+') {
                result = num1 + num2;
            } else if (operation === '-') {
                result = num1 - num2;
            }
            
            // გამოგვიტანოს 
            document.getElementById('result').innerText =  ${result}`;
        }
    </script>
</body>
</html>
