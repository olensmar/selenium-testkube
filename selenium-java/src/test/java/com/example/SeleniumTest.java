package com.example;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class SeleniumTest {
    @Test
    public static void main(String[] args) {
        System.out.println("Test Execution Started");

        // Set the path to the chromedriver executable
//        System.setProperty("webdriver.chrome.driver", "/usr/local/bin/chromedriver");

        // Initialize ChromeOptions
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--ignore-ssl-errors=yes");
        options.addArguments("--headless");
        options.addArguments("--no-sandbox");
        options.addArguments("--ignore-certificate-errors");

        WebDriver driver = null;

        try {
            // Initialize the Chrome driver with options
            driver = new ChromeDriver(options);

            // Maximize the window size
            driver.manage().window().maximize();
            System.out.println("Timer1");

            // Sleep for 5 seconds
            Thread.sleep(5000);

            // Navigate to the blog
            driver.get("https://cerebro1.github.io/");
            System.out.println("Get Successful");

            // Sleep for 5 seconds
//            Thread.sleep(5000);

            // Click on the About button
            WebElement about = driver.findElement(By.linkText("About"));
            about.click();
            System.out.println("Click Successful");

            // Sleep for 5 seconds
//            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            if (driver != null) {
                driver.close();
                driver.quit();
            }
            System.out.println("Test Execution Successfully Completed!");
        }
    }
}
