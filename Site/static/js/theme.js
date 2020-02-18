let theme = localStorage.getItem('theme');
var checkTheme = document.querySelector('input[name=theme]');

const enableDarkTheme = function() {
    document.documentElement.setAttribute('data-theme', 'dark');
    document.getElementById("checkTheme").classList.remove('btn-light');

    localStorage.setItem('theme', 'dark');
};

const enableLightTheme = function() {
    document.documentElement.setAttribute('data-theme', 'light');
    document.getElementById("checkTheme").classList.add('btn-light');

    localStorage.setItem('theme', 'light');
};

if (theme === 'dark') {
    enableDarkTheme();
}

checkTheme.addEventListener('change', function() {
    let theme = localStorage.getItem('theme');

    if(theme === 'dark') {
        enableLightTheme();
    } else {
        enableDarkTheme();
    }
});