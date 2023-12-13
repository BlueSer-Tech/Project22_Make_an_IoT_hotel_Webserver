$(document).ready(function(){
function sendRequest(){
    $.ajax({
        url: '',
        type: "POST",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({room: $('#room').val(), time: $('#time').val(), verify: $('#verify').val()}),
        success:
        function(result){
        var notice = "Đã có khách hàng mã CCCD là: " + result.pile_cccd + "chọn " + result.pile_room + ", ngày lưu trú: " + result.pile_start_day +
        ", số ngày lưu trú: " + result.pile_leng_stay + ", ngày trả phòng: " + result.pile_end_day
        + ", số tiền: " + result.pile_total_money;
        $('#cccd1').text(result.cccd1);$('#name1').text(result.name1);$('#room1').text(result.room1);
        $('#cccd2').text(result.cccd2);$('#name2').text(result.name2);$('#room2').text(result.room2);
        if(result.room == 'room1' || result.room == 'room2'){
            if  (confirm("Đã có khách hàng chọn phòng") == true){
            $('#room').val(result.room);
            $('#time').val(result.time);
                }
                }else{
                $('#room').val('refuse');
                $('#time').val('refuse');}

        if(result.custom_request == "YES")
        {
            if  (confirm(notice) == true){
                $('#verify').val('COMPLETE');
            }
        }
        else{
                $('#verify').val('refuse');
            }
        }
        ,
        complete:function(result){
                  setTimeout(sendRequest,1000);}
});
}

 $(document).ready(function()
  {
     setTimeout(sendRequest,1000);
    });
});
