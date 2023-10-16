
        // Sample data for the first pie chart
var data1 = {
    labels: ["provider1", "provider2", "provider3"],
    datasets: [{
      data: [30, 20, 50],
      backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
    }]
  };
  
  // Sample data for the second pie chart
  var data2 = {
    labels: ["customer1", "customer2", "customer3"],
    datasets: [{
      data: [25, 35, 40],
      backgroundColor: ["#4CAF50", "#9B59B6", "#FFA500"],
    }]
  };
  
  var options = {
    responsive: true,
    maintainAspectRatio: false,
  };
  
  // Render the first pie chart
  var ctx1 = document.getElementById("myPieChart").getContext("2d");
  var myPieChart1 = new Chart(ctx1, {
    type: 'pie',
    data: data1,
    options: options
  });
  
  // Render the second pie chart
  var ctx2 = document.getElementById("myPieChart2").getContext("2d");
  var myPieChart2 = new Chart(ctx2, {
    type: 'pie',
    data: data2,
    options: options
  });
  
  let sidebar = document.querySelector(".sidebar");
  let sidebarBtn = document.querySelector(".sidebarBtn");
  sidebarBtn.onclick = function() {
    sidebar.classList.toggle("active");
    if (sidebar.classList.contains("active")) {
      sidebarBtn.classList.replace("bx-menu", "bx-menu-alt-right");
    } else {
      sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
    }
  };
  