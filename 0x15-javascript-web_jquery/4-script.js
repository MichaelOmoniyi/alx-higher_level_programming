function toggleHeaderColor()
{
    if ($('HEADER').hasClass('red'))
    {
        $('HEADER').removeClass('red').addClass('green');
    }
    else
    {
        $('HEADER').removeClass('green').addClass('red');
    }
}
