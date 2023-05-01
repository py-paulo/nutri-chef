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

$("#client-search").on("input", function() {
  let search_value = $(this).val();
  let cards = $('.card');
  for (let index = 0; index < cards.length; index += 1) {
    let card = cards[index];
    let client_name = card.getAttribute('data-client-name');
    if (client_name.toLowerCase().startsWith(search_value.toLowerCase())) {
      card.classList.remove("hidden");
    } else {
      card.classList.add("hidden");
    }
  }
});

$("#catalog-search").on("input", function() {
  let search_value = $(this).val();
  let cards = $('.card');
  for (let index = 0; index < cards.length; index += 1) {
    let card = cards[index];
    let recipe_name = card.getAttribute('data-recipe-name');
    if (recipe_name.toLowerCase().startsWith(search_value.toLowerCase())) {
      card.classList.remove("hidden");
    } else {
      card.classList.add("hidden");
    }
  }
});
