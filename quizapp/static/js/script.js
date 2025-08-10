function validQuiz(){
    const form = document.querySelector("form");
    const questions = document.querySelectorAll(".question-block")

    for(let question of questions){
        const inputs = question.querySelectorAll("input[type='radio']");
        let answered = false;

        for(let input of inputs){
            if(input.checked){
                answered=true;
                break;
            }
        }
        if(!answered){
            swal("Oops!", "Please select all answers before submitting.", "warning");
            return false;
        }
    
    }
    return true;
}


// Setting timer for quiz

let totalTime = 2*60;
function startTimer(){
    let timeInterval = setInterval(function(){
        let minutes = Math.floor(totalTime/60);
        let seconds = totalTime%60;
        document.getElementById("time").textContent  = `${minutes}:${seconds<10?'0':''}${seconds}`;
        totalTime--;

        if(totalTime<0){
            clearInterval(timeInterval);
            alert("⏳ Time is up! Submitting your quiz...");
            document.querySelector("form").submit()
        }
    },1000);
}
window.onload = startTimer;