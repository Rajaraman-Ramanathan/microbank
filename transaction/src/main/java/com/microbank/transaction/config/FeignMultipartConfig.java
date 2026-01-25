package com.microbank.transaction.config;

import org.springframework.boot.autoconfigure.http.HttpMessageConverters;
import org.springframework.cloud.openfeign.support.SpringEncoder;
import org.springframework.context.annotation.Bean;
import org.springframework.beans.factory.ObjectFactory;
import feign.codec.Encoder;

import feign.form.spring.SpringFormEncoder;

public class FeignMultipartConfig {

    @Bean
    public Encoder feignFormEncoder(
            ObjectFactory<HttpMessageConverters> converters
    ) {
        return new SpringFormEncoder(new SpringEncoder(converters));
    }
}
