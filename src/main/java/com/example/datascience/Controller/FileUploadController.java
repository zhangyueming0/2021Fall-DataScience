package com.example.datascience.Controller;


import com.example.datascience.Service.PythonService;
import com.example.datascience.Service.TextReadService;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;

/**
 * 文书上传控制类
 */

@RestController
public class FileUploadController {
    @RequestMapping("/fileUpload")
    /**
     *文书上传
     */
    public String upload(MultipartFile fileUpload) {
        //获取文书的文件名
        String filename = fileUpload.getOriginalFilename();
        try {
            assert filename != null;
            fileUpload.transferTo(new File(filename));
        } catch (IOException e) {
            e.printStackTrace();
        }
        String path = "src/main/resources/Documents/" + filename;
        TextReadService textReadService = new TextReadService();
        //文书内容读取（限txt,doc,docx）
        String text = "";
        if (filename.endsWith(".docx")) {
            text = textReadService.docxRead(path);
        } else if (filename.endsWith(".doc")) {
            text = textReadService.docRead(path);
        } else if (filename.endsWith(".txt")) {
            text = textReadService.txtRead(path);
        }
        //执行python程序对文书内容进行分词处理
        PythonService pythonService = new PythonService();
        pythonService.process1(text);
        pythonService.process2(text);
        return "文件上传成功！请返回上级界面！";
    }

}
