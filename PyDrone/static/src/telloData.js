// https://stackoverflow.com/questions/42601478/flask-calling-python-function-on-button-onclick-event

function commandMaker(id, url) {
     $(function () {
          $(`a#${id}`).on('click', function (e) {
               // stops refresh
               e.preventDefault()
               // gets json(converted) data from url
               $.getJSON(`${url}`,
                    function (data, textStatus) {
                         console.log(data)
                    });
          })
     })
}

commandMaker('takeOff', '/takeOff')
commandMaker('land', '/land')
commandMaker('connect', '/connect')
commandMaker('stream', '/stream')

