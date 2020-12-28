library(NutrienTrackeR)

# save each countries food database
US_df <- (NutrienTrackeR::food_composition_data$USDA) 
FR_df <- (NutrienTrackeR::food_composition_data$CIQUAL)
SP_df <- food_composition_data$BEDCA

labels <- read.table(file = 'labels.txt', sep = '\n')$V1 # read our labels in

desired_features_FR <- colnames(FR_df)[c(5,7,8,9,10,35)]
desired_features_FR

desired_features_US <- colnames(US_df)[c(6,7,10,8,12,18)]
desired_features_US

desired_features_SP <- colnames(SP_df)[c(6,7,14,9,10,45)]
desired_features_SP

extract_nutrients <- function(x){
  # find all the results for our desired food
  search_results <- rbind(US_df[grepl(x, US_df[,'food_name'], ignore.case = TRUE), desired_features_US],
                          FR_df[grepl(x, FR_df[,'food_name'],, ignore.case = TRUE), desired_features_FR],
                          SP_df[grepl(x, SP_df[,'food_name'],, ignore.case = TRUE),desired_features_SP])
  mode(search_results) <- "numeric" # make sure all values are numeric
  output <- apply(search_results, MARGIN = 2, mean, na.rm = TRUE) # take the average of these results
  
  if (length(output) < 6){ # if the length of our output is less than 6 (i.e. no results were found, then fill it  with NAs)
    length(output) <- 6
    output[] <- NA
  }
  output
}

# use vectorisation to apply the function to all nutrients
nutrients <- t(vapply(labels, extract_nutrients, FUN.VALUE = numeric(6)))

which(is.na(nutrients[,1]))

# Fill in the missing data - manually
nutrients[2,] <- extract_nutrients("Ribs")
nutrients[5,] <- extract_nutrients("tartare")
nutrients[6,] <- extract_nutrients("Beet")
nutrients[7,] <- extract_nutrients("Fritter")
nutrients[8,] <- extract_nutrients("Kimchi")
nutrients[9,] <- extract_nutrients("pudding")

which(is.na(nutrients[,1]))

synonyms_for_missing <- c("Tomato Bread",
                          "Caesar",
                          "Fried Pastry", "Caprese", "Cake", "Raw fish", 
                          "Curry", "Quesadilla", "Wings", "churro", "egg sandwich",
                          "cupcake", "egg", "donut", "benedict", "escargot", "fish finger", 
                          "onion soup", "calamari", "Greek", "cheese sandwich", 
                          "Salmon", "Guac", "dumpling", "hot and sour", "Huevos", 
                          "Lobster", "lobster roll", "macaron", "oyster", "rice noodles",
                          "duck", "pork", "fries", "rib", "pulled pork", "velvet","raw fish", "seaweed",
                          "shrimp","bolognese",
                          "carbonara", "spring", "shortcake", "taco", "octopus", "tartare")

fill_na <- t(vapply(synonyms_for_missing, extract_nutrients, FUN.VALUE = numeric(6)))

nutrients[is.na(nutrients[,1]), ] <- fill_na

# Now we have much less things to actually fill in manually
which(is.na(nutrients[,1]))
nutrients[11,] <- extract_nutrients("bru") #partial searching

nutrients[13,] <- extract_nutrients("Cann") #partial searching

nutrients[14,] <- extract_nutrients("salad") #partial searching

nutrients[16,] <- extract_nutrients("marinate")

nutrients[21,] <- extract_nutrients("wing")

nutrients[24,] <- extract_nutrients("doughnuts")

nutrients[29,] <- extract_nutrients("egg")

nutrients[30,] <- extract_nutrients("cake")

nutrients[32,] <- extract_nutrients("doughnuts")

nutrients[36,] <- extract_nutrients("snail")

nutrients[39,] <- extract_nutrients("cutlet")

nutrients[42,] <- extract_nutrients("soup")

nutrients[44,] <- extract_nutrients("squid")

nutrients[50,] <- extract_nutrients("grilled cheese")

Gucamole <- extract_nutrients("Guaca")
Gucamole[1] <- 4 * Gucamole[2] + 9 *Gucamole[4] + 4 *Gucamole[3] # using the formula for calories
nutrients[52,] <- Gucamole

nutrients[57,] <- extract_nutrients("poached")

nutrients[62,] <- extract_nutrients("lobster")

nutrients[87,] <- extract_nutrients("raw")

write.csv(nutrients, "label_nutrients.csv")











