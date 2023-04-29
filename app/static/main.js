$('.image').dimmer({
  on: 'hover'
});

$('.detail').on("click", function() {
  let client_id = $(this).attr('client-id');
  window.location.replace(`/clients/${client_id}`);
});