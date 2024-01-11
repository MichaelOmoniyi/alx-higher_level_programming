$(document).ready(function () {
    const baseUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
    
    $('INPUT#btn_translate').click(function () {
        const languageCode = $('INPUT#language_code').val();
        const url = baseUrl + '?' + $.param({ lang: languageCode });

        $.get(url, function (data) {
            $('DIV#hello').text(data.hello);
        });
    });
});
