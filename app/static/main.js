$('.image').dimmer({
  on: 'hover'
});

$('.detail').on("click", function() {
  let client_id = $(this).attr('client-id');
  window.location.replace(`/clients/${client_id}`);
});

$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;

$('.delete')
  .on('click', function() {
    let food_name = $(this).attr('data-value');
    $('#delete-food-name').val(food_name);
    $('.ui.basic.modal').modal('show');
  });