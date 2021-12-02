$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "https://api.manana.kr/exchange/rate.json",
        data: {},
        success: function (response) {
            let nowRate = response[1]['rate'];
            $('#rate-box').text(nowRate);
        }
    })
    order_listing();
});

function order_listing() {
    // 주문목록 보기 API 연결
    $.ajax({
        type: "GET",
        url: "/order",
        data: {},
        success: function (response) {
            let orders = response['all_orders'];

            for (let i = 0; i < orders.length; i++) {
                let name = orders[i]['name'];
                let phone = orders[i]['phone'];
                let address = orders[i]['address'];
                let count = orders[i]['count'];

                let temp_html = `    <tr>
      <th scope="row">${name}</th>
      <td><center>${count}</center></td>
      <td>${address}</td>
      <td>${phone}</td>
    </tr>`;
                $('#tbody_insert').append(temp_html);
            }
        }

    })
}

function order() {
    // 주문하기 API 연결
    let address = $('#order-address').val()
    let name = $('#order-name').val()
    let count = $('#order-count').val()
    let phone = $('#order-phone').val()
    $.ajax({
        type: "POST",
        url: "/order",
        data: {
            address: address,
            name: name,
            count: count,
            phone: phone,
        },
        success: function (response) { // 성공하면
            alert("주문 완료!");
            window.location.reload();
        }
    })
}
