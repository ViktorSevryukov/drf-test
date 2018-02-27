$(document).ready(function () {

    //add bootstrap class for inputs
    $('input[type="text"]').addClass('form-control');
    $('input[type="file"]').addClass('form-control-file');

    // add datepicker to input field
    $('#id_birth_date').prop(
        {
            'data-provide': 'datepicker',
            'readonly': true
        }
    ).datepicker({
        weekStart: 1
    })
});
