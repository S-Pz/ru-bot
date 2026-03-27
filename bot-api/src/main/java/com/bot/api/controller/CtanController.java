package com.bot.api.controller;

import com.bot.api.entity.Ctan;

import com.bot.api.service.CtanService;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping("/ctan")
@CrossOrigin(origins = "*")
public class CtanController {
    
    private final CtanService ctanService;

    public CtanController(CtanService ctanService){
        this.ctanService = ctanService;
    }

    @PostMapping()
    public ResponseEntity<List<Ctan>> crate(@RequestBody List<Ctan> ctan) {
        List<Ctan> salvo = ctanService.crate(ctan);

        for (int i = 0; i< salvo.size(); i++){
            System.out.println("Payload " + salvo.get(i).toString());
        }

        return ResponseEntity.status(HttpStatus.CREATED).body(salvo);
    }
    
}
