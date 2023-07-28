window.addEventListener("DOMContentLoaded", function () {
  var parent = document.querySelector(".parent");
  var child = document.querySelector(".child");
  var isMouseDown = false;
  var offsetX = 0;
  var offsetY = 0;

  child.addEventListener("mousedown", function (e) {
    isMouseDown = true;
    offsetX = e.clientX - child.offsetLeft;
    offsetY = e.clientY - child.offsetTop;
  });

  window.addEventListener("mouseup", function () {
    isMouseDown = false;
  });

  parent.addEventListener("mousemove", function (e) {
    if (isMouseDown) {
      child.style.left = e.clientX - offsetX + "px";
      child.style.top = e.clientY - offsetY + "px";
    }
  });
});
// .parent {
//   position: relative;
//   width: 400px;
//   height: 300px;
//   border: 1px solid #ccc;
//   margin: 50px auto;
// }

// .child {
//   position: absolute;
//   top: 20px;
//   left: 20px;
//   width: 200px;
//   height: 100px;
//   background-color: #f0f0f0;
//   border: 1px solid #999;
//   cursor: move;
// }