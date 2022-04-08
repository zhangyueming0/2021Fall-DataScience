package com.example.datascience.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Python脚本方法的实现类
 */
public class PythonService implements Python {
    /**
     * 获取人物基本信息的方法
     * @param text 文书内容
     */
    public void process1(String text) {
        String result = "";
        try {
            String[] args = new String[]{"D:\\Python38\\python.exe", "C:\\Users\\dell\\Desktop\\DataScience\\src\\main\\resources\\static\\python\\keywordExtraction1.py", text};
            Process process = Runtime.getRuntime().exec(args);
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream(), "GBK"));
            String line = "";
            while ((line = in.readLine()) != null) {
                result += line + "\n";
            }
            in.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    /**
     * 获取词性的方法
     * @param text 文书内容
     */
    public void process2(String text) {
        String result = "";
        try {
            String[] args = new String[]{"D:\\Python38\\python.exe", "C:\\Users\\dell\\Desktop\\DataScience\\src\\main\\resources\\static\\python\\keywordExtraction2.py", text};
            Process process = Runtime.getRuntime().exec(args);
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream(), "GBK"));
            String line = "";
            while ((line = in.readLine()) != null) {
                result += line + "\n";
            }
            in.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
