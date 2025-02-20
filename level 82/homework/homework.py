<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 50px;
        }
        #timer {
            font-size: 48px;
            margin-top: 20px;
        }
        #message {
            font-size: 32px;
            color: red;
            margin-top: 20px;
        }
        input {
            font-size: 20px;
            padding: 5px;
        }
        button {
            padding: 10px 20px;
            font-size: 18px;
            cursor: pointer;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>დროის დამთვლელი</h1>
    <label for="timeInput">შეიყვანეთ დრო (მილიწამი): </label>
    <input type="number" id="timeInput" min="0" max="10000">
    <br>

    <button id="startBtn">Start</button>
    <button id="stopBtn" disabled>Stop</button>

    <div id="timer"></div>
    <div id="message"></div>

    <script>
        let timerInterval;
        let currentCount = 0;
        let totalTime = 0;
        const timerElement = document.getElementById("timer");
        const messageElement = document.getElementById("message");
        const timeInput = document.getElementById("timeInput");
        const startBtn = document.getElementById("startBtn");
        const stopBtn = document.getElementById("stopBtn");

        startBtn.addEventListener("click", () => {
            totalTime = parseInt(timeInput.value);
            if (isNaN(totalTime) || totalTime <= 0) {
                alert("გთხოვთ, შეიყვანოთ დადებითი მთელი რიცხვი");
                return;
            }

            currentCount = 1;
            messageElement.textContent = '';
            timerElement.textContent = currentCount;
            startBtn.disabled = true;
            stopBtn.disabled = false;

            timerInterval = setInterval(() => {
                if (currentCount >= totalTime) {
                    clearInterval(timerInterval);
                    messageElement.textContent = "Time's up!";
                    startBtn.disabled = false;
                    stopBtn.disabled = true;
                } else {
                    currentCount++;
                    timerElement.textContent = currentCount;
                }
            }, 1000);
        });

        stopBtn.addEventListener("click", () => {
            clearInterval(timerInterval);
            startBtn.disabled = false;
            stopBtn.disabled = true;
            messageElement.textContent = 'გათიშულია';
            timerElement.textContent = '';
        });
    </script>
</body>
</html>
