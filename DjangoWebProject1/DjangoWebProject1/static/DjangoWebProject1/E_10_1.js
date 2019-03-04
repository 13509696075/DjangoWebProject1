$(document).ready(function() {
    $('#bn').click(function () {
        var amount = $("#amount").val();
        var rate = $("#rate").val();
        var period = $("#period").val();
        $.ajax({
            type: 'GET',
            url: "/result",
            data: {
                'amount': amount,
                'rate': rate,
                'period': period
            },
            success: function (Data) { /*假设后端执行“成功”后，做以下动作（Data是回传内容）*/
                $("#result").html(Data)
            },
            error: function (e) {
                console.log(e);
            }
        })
    });
});