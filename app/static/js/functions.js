function message_error(obj) {
    var html = '<ul style="text-align: left;">';
    if (typeof (obj) === 'object') {
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    }
    else {
        html += '<p>'+obj+'</p>';
    }
    Swal.fire({
        title: 'Error',
        html: html,
        icon: 'error'
    });
}