package com.example.datascience.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * 跳转不同页面的控制类
 */
@Controller
public class ToPageController {

    @RequestMapping("/index.html")
    public String myindex() {
        return "index";
    }

    @RequestMapping("/upload.html")
    public String upload() {
        return "upload";
    }

    @RequestMapping("/sign.html")
    public String sign() {
        return "sign";
    }

    @RequestMapping("/analyze.html")
    public String analyze() {
        return "analyze";
    }
}
