package com.example.datascience.Controller;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

/**
 * json文件的绝对地址与虚拟地址的映射控制类
 */
@Configuration
public class URLConfigController extends WebMvcConfigurerAdapter {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        //handler为前台访问的目录，locations为files相对应的本地路径
        registry.addResourceHandler("/templates/json/**").addResourceLocations("file:/C:/Users/dell/Desktop/DataScience/src/main/resources/templates/");
        super.addResourceHandlers(registry);
    }
}

