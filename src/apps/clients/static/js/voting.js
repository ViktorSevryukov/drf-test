const baseAPIUrl = '/api/v1/clients/';
const maxRating = 10;

/* Helper function to make api call */
function apiCall(url, data, callback) {
    $.ajax({
        url: baseAPIUrl + url,
        data: data,
        success: callback,
        dataType: 'json'
    })
}

/* Change text of 'rating' element*/
function setRating(pk, value) {
    var elId = 'client-' + pk + '-rating';
    $('#' + elId).text(value)
}

/* Vote for photo */
function vote(button, pk) {
    // hide button and show loader
    $(button).hide();
    var loader = $('#loader-'+pk);
    loader.show();

    var url = pk + '/vote/';
    // send request to api
    apiCall(url, {}, function (data) {
        setRating(pk, data['rating']);
        // hide loader and show button, if new rating value < maxRating value
        loader.hide();
        if (data['rating'] < maxRating) $(button).show();
    })
}
