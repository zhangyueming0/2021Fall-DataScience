package com.example.datascience.Service;

import java.io.*;
import java.io.FileInputStream;
import java.io.InputStream;

import org.apache.poi.POIXMLDocument;
import org.apache.poi.POIXMLTextExtractor;
import org.apache.poi.hwpf.extractor.WordExtractor;
import org.apache.poi.openxml4j.opc.OPCPackage;
import org.apache.poi.xwpf.extractor.XWPFWordExtractor;

/**
 *文书内容读取类
 */
public class TextReadService {
    /**
     * txt格式的文书内容读取的方法
     * @param path 文书的本地地址路径
     * @return 文书内容
     */
    public String txtRead(String path) {
        try {
            BufferedReader buf = new BufferedReader(new FileReader(path));
            StringBuffer sbuf = new StringBuffer();
            String line = null;
            while ((line = buf.readLine()) != null) {
                sbuf.append(line);
            }
            buf.close();
            return sbuf.toString();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * doc格式的文书内容读取的方法
     * @param path 文书的本地地址路径
     * @return 文书内容
     */
    public String docRead(String path) {
        try {
            InputStream is = new FileInputStream(path);
            WordExtractor ex = new WordExtractor(is);
            return ex.getText();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
    /**
     * docx格式的文书内容读取的方法
     * @param path 文书的本地地址路径
     * @return 文书内容
     */
    public String docxRead(String path) {
        try {
            OPCPackage opcPackage = POIXMLDocument.openPackage(path);
            POIXMLTextExtractor extractor = new XWPFWordExtractor(opcPackage);
            return extractor.getText();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
