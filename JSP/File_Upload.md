# File Upload

* 라이브러리를 사용한 파일 업로드



## Download and Apply

1. (링크)["http://www.servlets.com"]
2. WEB-INF/lib에 복사



## Upload

* WebContent에 파일이 저장될 폴더 생성
* `enctype`: `"multipart/form-data"`로 설정 (`HTML`)

```jsp
<%@pate import "com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<%@pate import="com.oreilly.servlet.MultipartRequest"%>

<%
	String path = request.getRealPath("fileFolder");
	int size = 1024 * 1024 * 10; //10M
	String file = "";
	String oriFile = "";
	try{
        MultipartRequest multi = new MultipartRequest(request, path, size, "EUC-KR", new DefaultFileRenamePolicy());
        
        Enumeratation files = multi.getFileNames();
        String str = (string)files.getnextElement();
        
        file = multi.getFilesystemName(str);
        oriFile = multi.getOriginalFileName(str);
    }catch (Exception e){
        e.printStackTrace();
    }
```

