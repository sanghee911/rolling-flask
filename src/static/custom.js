$(document).ready(function() {

    window.setInterval( function() {
        $.ajax({
            // data: {'query_string': queryString},
            url: 'http://localhost:8080',
            type: 'get',
            contentType: "application/json; charset=utf-8",
            success: function(data) {
                console.log(data);
                    // var hostname = data.Hostname;
                    // var color = data.Color;
                    //
                    // $('.server').html(hostname);
            }
        });
        // console.log('test');
    }, 1000);

});
