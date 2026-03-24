package com.bot.api.repository;

import com.bot.api.entity.Ctan;

import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;
import java.util.Optional;

public interface CtanRepository extends JpaRepository<Ctan, Long>{
    Optional<Ctan> findByData(LocalDate data);
}
