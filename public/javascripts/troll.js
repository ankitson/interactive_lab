(function ($) {

  $.fn.extend({

    textFX: function (message, options) {

      var defaults = {
        delay: 0,
        mspl: 40
      };

      var settings = $.extend(defaults, options);
      var letters = message.split('');

      var shuffle = function () {
          return Math.random() < 0.5 ? 1 : -1;
        };

      return this.each(function () {

        var $this = $(this);
        var order = [],
          output = [];
        var length = letters.length;

        $this.text('');

        for (var i = 0; i < length; i++) {
          output[i] = Math.random() < 0.1 ? '<span class="dud">|</span>' : '';
          order[i] = i;
        }

        order.sort(shuffle);

        var o = {
          t: 0
        };
        var n, p;

        $(o).delay(settings.delay).animate({
          t: 1
        }, {
          duration: settings.mspl * length,
          step: function () {
            p = Math.floor(o.t * length);
            if (order[p] !== null) {
              n = order[p];
              output[n] = letters[n];
              order[p] = null;
            }
            $this.html(output.join(''));
          },
          complete: function () {
            $this.html(message);
          }
        });

      });
    }
  });
})(jQuery);

function randomDigit() {
	return Math.round(Math.random());
}

function randomBinaryString(len) {
	var string="";
	for (var i=0; i<len; i++)
		string+=randomDigit();
	return string;
}
function go() {
  $('#tf1').textFX("buttsecks is the best secks...", {
    delay: 0
  });
  $('#tf2').textFX("but what is the definition of buttsecks?", {
    delay: 1000
  });
  $('#tf3').textFX("maybe life is all just a big game of buttsecks", {
    delay: 1500
  });
  $('#tf4').textFX("were all in it, were all in each other", {
    delay: 1800
  });
  $('#tf5').textFX("Does it bother you that you're not real?", {
    delay: 2000
  });
	$('#tf6').textFX("Does it bother you that we're not real?", {
    delay: 2200
  });
  $('#tf7').textFX("Does it bother you that NOTHING IS real?", {
    delay: 2400
  });
  $('#tf8').textFX("nothing is real", {
    delay: 2500
  });
  $('#tf9').textFX("THE MATRIX HAS YOU", {
    delay: 2600
  });
  $('#tf10').textFX("THERE IS NO ESCAPE", {
    delay: 2700
  });
  $('#tf11').textFX("THERE IS NO ESCAPE", {
    delay: 2700
  });
  
  var strings = [ randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000) ,randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000), randomBinaryString(1000)]
  $('#tf1').textFX(strings[0], {
    delay: 5000
  });
  $('#tf2').textFX(strings[1], {
    delay: 5000
  });
  $('#tf3').textFX(strings[2], {
    delay: 5000
  });
  $('#tf4').textFX(strings[3], {
    delay: 5000
  });
  $('#tf5').textFX(strings[4], {
    delay: 5000
  });
  $('#tf6').textFX(strings[5], {
    delay: 5000
  });
  $('#tf7').textFX(strings[6], {
    delay: 5000
  });
  $('#tf8').textFX(strings[7], {
    delay: 5000
  });
  $('#tf9').textFX(strings[8], {
    delay: 5000
  });
  $('#tf10').textFX(strings[9], {
    delay: 5000
  });
	$('#tf11').textFX(strings[10], {
    delay: 5000
  }); 
  $('#tf12').textFX(strings[11], {
    delay: 5000
  });
  $('#tf13').textFX(strings[12], {
    delay: 5000
  });
  $('#tf14').textFX(strings[13], {
    delay: 5000
  });
  $('#tf15').textFX(strings[14], {
    delay: 5000
  });
  $('#tf16').textFX(strings[15], {
    delay: 5000
  });
  $('#tf17').textFX(strings[16], {
    delay: 5000
  });
  $('#tf18').textFX(strings[17], {
    delay: 5000
  });
    $('#tf19').textFX(strings[18], {
    delay: 5000
  });
    $('#tf20').textFX(strings[19], {
    delay: 5000
  });
    $('#tf21').textFX(strings[20], {
    delay: 5000
  });
    $('#tf2').textFX(strings[21], {
    delay: 5000
  });
    $('#tf23').textFX(strings[22], {
    delay: 5000
  });

};

$('#btn').click(function () {
  go();
  return false;
});

go();