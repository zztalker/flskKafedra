var pathname = window.location.pathname;

// MAIN HEADER
$("a[link='" + pathname + "']").parent().attr("class", "active");

var tags = [
	"Безопасность - не предел!",
	"Не всякий может смотреть в будущее",
	"Мы лучше всех знаем, что Вам нужно!",
	"Мы не следим, мы интересуемся",
	"Мы опаснее преступников",
	"Сила, дисциплина, стиль",
	"Мы знаем, что Вы делали прошлым летом...",
	"365/12/24/7"
];
var tag = tags[Math.floor(Math.random() * tags.length)];
$("#navBarText").text(tag);

// Redirect Buttons
$(".redirectButton").click(function (element) {
	var link = element.currentTarget.attributes.link.nodeValue;
	if (pathname === link) { }
	else {
		$("#content").LoadingOverlay("show", {
		image: "/static/img/loading.gif"
		});
		document.location.pathname = link;
	}
});