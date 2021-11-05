function setOrder(orderList) {
  console.log(orderList)
  for (var i = 0; i < orderList.length; i++) {
    var order = orderList[i]
    $("div").find("#" + order.name).css({order: i + 1});
  }
}

function getModelData() {
  var models = [];
  var boxes = $("div").find('[aria-type="model-box"]')
  for (var i = 0; i < boxes.length; i++) {
    var box = $(boxes[i]);
    var data = {
      name: box.data("name"),
      fps: box.data("fps"),
      resolution: box.data("resolution"),
    }
    models.push(data)
  }
  return models;
}

function sortByName(asc) {
  const models = getModelData()
  models.sort(function(a, b) {
      if(a.name < b.name) { return -1; }
      if(a.name > b.name) { return 1; }
      return 0;
  });
  setOrder(models)
}