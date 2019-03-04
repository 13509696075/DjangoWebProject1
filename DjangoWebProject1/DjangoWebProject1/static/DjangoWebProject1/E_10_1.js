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
            success: function (Data) { /*������ִ�С��ɹ����������¶�����Data�ǻش����ݣ�*/
                $("#result").html(Data)
            },
            error: function (e) {
                console.log(e);
            }
        })
    });
});