/* jshint browser: true, devel: true */
/* global grp */

(function($) {
  'use strict';
  $(document).ready(function() {

    // Set this to the name of the column holding the position
    var posField = 'position';

    // Determine the column number of the position field
    var posColumn = null;

    var cols = $('.grp-changelist-results tbody tr:first').children();

    for (var i = 0; i < cols.length; i++) {
      var inputs = $(cols[i]).find('*').filter(function() {
        return /^form(.*?)position$/.test($(this).attr('name'));
      });

      if (inputs.length > 0) {
        // Found!
        posColumn = i;
        break;
      }
    }

    if (posColumn === null) {
      return;
    }

    // Hide position field
    $('.grp-changelist-results tbody tr').each(function() {
      var posCell = $(this).children()[posColumn];
      var input = $(posCell).children('input').first();
      input.hide();
    });

    // Determine sorted column and order
    var sorted = $('.grp-changelist-results thead th.sorted');
    var sortedCol = $('.grp-changelist-results thead th').index(sorted);
    var sortOrder = sorted.hasClass('descending') ? 'desc' : 'asc';

    $('.grp-changelist-results tbody tr').each(function() {
      var posCell = $(this).children()[posColumn];
      var input = $(posCell).children('input').first();
      var label = $('<strong>' + input.attr('value') + '</strong>');
      $(posCell).append(label);
    });

    if (sortedCol !== posColumn) {
      // Sorted column is not position column, show position and bail out
      return;
    }

    // add drag icons
    $('.grp-changelist-results tbody tr').each(function() {
      var posCell = $(this).children()[posColumn];
      var dragIcon = $(
        '<ul class="grp-tools" style="top: -4px; margin-right: -7px; padding-right: 0">' +
        '<li><a href="javascript://" class="grp-icon grp-drag-handler" title="Move Item"></a></li>' +
        '</ul>'
      );
      $(posCell).append(dragIcon);
    });

    $('.grp-changelist-results tbody').sortable({
      axis: 'y',
      items: 'tr',
      cursor: 'move',
      update: function() {
        var items = $(this).find('tr').get();

        if (sortOrder === 'desc') {
          // Reverse order
          items.reverse();
        }

        $(items).each(function(index) {
          var posCell = $(this).children()[posColumn];
          var input = $(posCell).children('input').first();
          var label = $(posCell).children('strong').first();

          input.attr('value', index);
          label.text(index);
        });

        // Update row classes
        $(this).find('tr').removeClass('row1').removeClass('row2');
        $(this).find('tr:even').addClass('row1');
        $(this).find('tr:odd').addClass('row2');
      }
    });

    // Broken table fix. Seems to collide with internal css.
    $('tbody.ui-sortable').removeClass('ui-sortable');
  });
})(grp.jQuery);
