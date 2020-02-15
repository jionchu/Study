# Upload file - Multipart
파일을 전송하기 위해서는 일반적인 Request로는 불가능하다. 파일을 전송하기 위해서는 form-data 형식이 되어야 하고 일반 request는 x-www-form-urlencoded이기 때문에 MultipartBody를 이용해야 한다. 일반 Request로 하면 값을 제대로 전달하지 못하고 에러가 남  
