// console.log("Тест");
const url = window.location.href

const quizBox = document.getElementById('quiz-box');
// let data;

const scoreBox = document.querySelector('#score-box');
const resultBox = document.querySelector('#result-box');

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        // console.log(response);
        const data = response.data;
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)) {
                // console.log(question);
                // console.log(answers);
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                    <div>
                        <input type="radio" class="ans" 
                        id="${question}-${answer}" 
                        name="${question}" 
                        value=${answer}>
                        <label for="${question}">${answer}</label>
                    </div>
                `
            })
        }
    });
},
error: function (error) {
    console.log(error);
}
})

const quizForm = document.querySelector('#quiz-form');
const csrf = document.getElementsByName('csrfmiddlewaretoken');

const sendData = () => {
    const elements = [...document.querySelectorAll('.ans')];
    const data = {};
    data['csrfmiddlewaretoken'] = csrf[0].value;
    elements.forEach(el => {
        if (el.checked){
            data[el.name] = el.value;
        }
        else{
            if(!data[el.name]){
                data[el.name] = null;
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            // console.log(response);
            const results = response.results
            // console.log(results)
            quizForm.classList.add('not-visible');

            scoreBox.innerHTML = `<h5 class="res">${response.
                passed ? 'Вы успешно сдали тест!' : 'Ниже проходного балла.'}
            Ваш результат ${response.score.toFixed(2)}%</h5>`

            results.forEach(res => {
                const resDiv = document.createElement("div");
                for (const [question, resp] of Object.entries(res)){
                    resDiv.innerHTML += question;
                    const cls = ['container', 'p-3',  'h6'];
                    resDiv.classList.add(...cls);

                    if (resp == 'not answered'){
                        resDiv.innerHTML += '<br><b><i> | нет ответа</i></b>';
                        resDiv.classList.add('negative');
                    }
                    else{
                        const answer = resp['answered'];
                        const correct = resp['correct_answer'];

                        if (answer == correct){
                            resDiv.classList.add('positive');
                            resDiv.innerHTML += `<br><i> | верно: ${answer}</i>`;
                        }
                        else{
                            resDiv.classList.add('negative');
                            resDiv.innerHTML += `<br><b> | правильный ответ: ${correct}</b>`;
                            resDiv.innerHTML += `<b> | ваш ответ: ${answer}</b>`;
                        }
                    }
                }
                // const body = document.getElementsByTagName('BODY')[0];
                const body = document.body;
                // body.append(resDiv);
                resultBox.append(resDiv);
            })
        },
        error: function(error){
            console.log(error);
        }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault();
    sendData();
})
