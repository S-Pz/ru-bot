package com.bot.api.controller;

import com.bot.api.dto.CtanDTO;
import com.bot.api.entity.Ctan;

import com.bot.api.service.CtanService;

import java.time.LocalDate;
import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;


@RestController
@RequestMapping("/ctan")
@CrossOrigin(origins = "*")
public class CtanController {
    
    private final CtanService ctanService;

    public CtanController(CtanService ctanService){
        this.ctanService = ctanService;
    }

    @GetMapping
    public ResponseEntity<Ctan>findByHorarioAndData(@RequestParam String data, @RequestParam String horario) {

        Ctan result = ctanService.findByHorarioAndData(horario, LocalDate.parse(data));

        return result != null ? ResponseEntity.status(HttpStatus.OK).body(result) : ResponseEntity.status(HttpStatus.NOT_FOUND).body(result);
        
    }

    // @GetMapping
    // public ResponseEntity<List<Ctan>>findByDataAndHorario(
    //     @RequestParam String data,
    //     @RequestParam String horario) {
        
    //     System.out.println("Data " + data + " horario " + horario);
    //     List<Ctan>result = ctanService.findByDataAndHorario(LocalDate.parse(data), horario);

    //     return ResponseEntity.status(HttpStatus.FOUND).body(result);
    // }
    
    @PostMapping()
    public ResponseEntity<List<Ctan>> crate(@RequestBody List<CtanDTO> ctanDto) {
    
        List<Ctan> salvo = ctanService.crate(ctanDto);

        for (int i = 0; i< salvo.size(); i++){
            System.out.println("Payload " + salvo.get(i).toString());
        }

        return ResponseEntity.status(HttpStatus.CREATED).body(salvo);
    }
    
}
