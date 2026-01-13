package com.microbank.account.feign;

import com.microbank.account.config.FeignConfig;
import com.microbank.account.dto.response.UserResponse;
import com.microbank.account.response.BaseApiResponse;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;

@FeignClient(name = "auth-service", configuration = FeignConfig.class)
public interface AuthServiceClient {

    @GetMapping("/users/me")
    BaseApiResponse<UserResponse> getCurrentUser();

}