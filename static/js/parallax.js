var coefficient = 10;
$('.metro-scroll').scroll(function(e){
	var bgpos = Math.floor((this.scrollLeft/coefficient)*-1) + 'px 0px';
	$('body').css('background-position', bgpos);
});