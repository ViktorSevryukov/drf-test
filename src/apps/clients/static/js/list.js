const baseAPIUrl = '/api/v1/clients/';

$(document).ready(function () {

    //add bootstrap class for inputs
    $('select').addClass('form-control');
    $('input[type="text"]').addClass('form-control');

});


var exportButton = $('#export-button');
var loader = $('#export-loader');

/* Helper function to make api call */
function apiCall(url, data, callback) {
    $.ajax({
        url: baseAPIUrl + url,
        data: data,
        success: callback,
        dataType: 'json'
    })
}

var checkStatusInterval = null;

/* Stop checking tasks by interval */
function stopChecking(){
    if (checkStatusInterval !== null) clearInterval(checkStatusInterval);
}

/* Check states, hide/show elements */
function handleResponse(data) {
    if (data.code === 'STOP')
        stopChecking();

    if (data.code === 'SUCCESS' && typeof data.url !== 'undefined') {
        stopChecking();
        loader.hide();
        exportButton.show();
        // redirect to file
        window.location = location.origin + data.url;
    }
}

/* Call API for export clients */
function exportXLS() {
    exportButton.hide();
    loader.show();

    // start export...
    var url = 'export/';
    apiCall(url, {}, function (data) {
            handleResponse(data);
            if (typeof data.task_id !== 'undefined') {
                checkStatusInterval = setInterval(function () {
                    check(data.task_id)
                }, 2000);
            }
        }
    )
}

/* Check task */
function check(task_id) {
    var url = 'check_task/' + task_id;
    apiCall(url, {}, function (data) {
            handleResponse(data);
        }
    )
}

