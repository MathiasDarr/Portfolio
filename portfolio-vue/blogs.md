            snotel_content: `

            <h3> Project Description </h3>
            <p>
          
            In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each day, the USDA measures
                the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
                task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
                is made available through an API (implemented & deployed as Spring Boot application running on ECS Fargate as well a serverless API using
                AWS API Gateway * lambda) with routes for querying the data for specific locations over a range of dates.
            </p>
            <h3> Washington State Snowpack</h3>

            <p>
            Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
            in the state of the snowpack & it's impact on agriculture and the threat of wildfires.  The drought year of 2015 was of particular interest to me.

            <img src="https://dakobed.s3-us-west-1.amazonaws.com/snotel.png">  />

            </p>

            <h3> Data Analysis </h3>

            <p>
              To analyze the data, I queried DynamoDB & saved the data to json files for each location & each year, then implmented functions that created
              a PySpark dataframe from a selection of locations & years.  As an example of the data, I include a screenshot of the Spark Dataframe showing data for Lyman 
              Lake in 2015 in early June.  What these numbers show is a staggering lake of snowpack (which I recall because I was there in late June)
            </p>

          <h3> Data Query API </h3>

            <p>
              I expose this data to be queried by location through a serverless API with a lambda function making a query to DynamoDB.  The API is defined using
              swagger which also enables CORS to allow requests from the browser.  I had initially been using postgres, but something about writing a query such
              as SELECT * FROM snotel_table WHERE location = 'Lyman Lake' seemed inefficient.  It seemed as though a noSQL database would be far more efficient for supporting
              a query by the primary/hash key (location ID) & a range/sort key (date of measurement)    
            </p>

            <h3> Data returned from API plotted with D3JS </h3>
            
            <img src="https://dakobed.s3-us-west-1.amazonaws.com/snotel_data.png">  />
            `,  


            introduction:` In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each day, the USDA measures
                the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
                task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
                is made available through an API (implemented & deployed as Spring Boot application running on ECS Fargate as well a serverless API using
                AWS API Gateway * lambda) with routes for querying the data for specific locations over a range of dates. `,

            introduction_title: 'Project Desrption',
            motviation_title: 'Motivation',
            motivation:`Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
              in the state of the snowpack & it's impact on agriculture and the threat of wildfires.  The drought year of 2015 was of particular interest to me. `,
            methods_title: 'Methods',
            analysis: ` To analyze the data, I queried DynamoDB & saved the data to json files for each location & each year, then implmented functions that created
              a PySpark dataframe from a selection of locations & years.  As an example of the data, I include a screenshot of the Spark Dataframe showing data for Lyman 
              Lake in 2015 in early June.  What these numbers show is a staggering lake of snowpack (which I recall because I was there in late June)`,
            analysis_title: 'Analysis',

            archticture_title: 'Query Service Archtiecture',
            archtiecture : `
              I expose this data to be queried by location through a serverless API with a lambda function making a query to DynamoDB.  The API is defined using
              swagger which also enables CORS to allow requests from the browser.  I had initially been using postgres, but something about writing a query such
              as SELECT * FROM snotel_table WHERE location = 'Lyman Lake' seemed inefficient.  It seemed as though a noSQL database would be far more efficient for supporting
              a query by the primary/hash key (location ID) & a range/sort key (date of measurement)    

            `,
            snotel_project:`
              In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each day, the USDA measures
              the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
              task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
              is made available through an API (implemented & deployed as Spring Boot application running on ECS Fargate as well a serverless API using
              AWS API Gateway * lambda) with routes for querying the data for specific locations over a range of dates.

              Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
              in the state of the snowpack & it's impact on agriculture and the threat of wildfires.  The drought year of 2015 was of particular interest to me.

              To analyze the data, I queried DynamoDB & saved the data to json files for each location & each year, then implmented functions that created
              a PySpark dataframe from a selection of locations & years.  As an example of the data, I include a screenshot of the Spark Dataframe showing data for Lyman 
              Lake in 2015 in early June.  What these numbers show is a staggering lake of snowpack (which I recall because I was there in late June)

              I expose this data to be queried by location through a serverless API with a lambda function making a query to DynamoDB.  The API is defined using
              swagger which also enables CORS to allow requests from the browser.  I had initially been using postgres, but something about writing a query such
              as SELECT * FROM snotel_table WHERE location = 'Lyman Lake' seemed inefficient.  It seemed as though a noSQL database would be far more efficient for supporting
              a query by the primary/hash key (location ID) & a range/sort key (date of measurement)    
            `,

            music_project: `
            <h3> Project Description </h3>


            In this project I attempt to perform automatic music transcription, the process of taking raw audio of a musician playing and instrumentand outputting guitar tab or piano sheet music depending on the instrument.  This problem falls under the subfield of data science known as MIR (Music Information Retrieval). As an musician I am frequently faced with wanting to know how a particular piece of music is played.  This often occurs when I watch people perform covers of songs I want to learn on Youtube.  Woulden't it be great if I could get a transcription of what they are playing?
            
            <h2> Methods </h2>
            
            I attempt to reproduce the neural network archticture described by Manuel Minguez Carretero in his thesis. He proposes several neural network architectures for solving this problem, which he trained on the MusicNet database, an MIR dataset of piano recordings and sheet music.  In this project I instead train models using the GuitarSet & the Maestro datasets for performing guitar and piano transcription.
            
            <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/audio.png" height="120">

            <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/screenshot.png" width="740" height="350">
            
            I save the the transforms and processed annotation numpy arrays to S3 from where the are downloaded to the EC2 instance, and fed into a Keras generator   
            for training the neural network.  The annotation labels of MusicNet are GuitarSet are similar. For each note they provide the following features
            * note start time
            * note end time
            * note (These are represented by MIDI values for each dataset though the MusicNet's have been rounded to integers while 
            the GuitarSet's have not.  However owing to the fact that piano sheet music encapsulates more information (most notably
            note durations such as quarter notes, half notes whole notes etc) than does guitar tablature, the MusicNet labels has 
            additional features (note length, measure and beat) than does the GuitarSet. My earlier attempts ignored this feature, 
            however eventually I decided to attempt to populate the missing feature by solving an unsupervised learning problem.  

            <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/cnn.png" width="560" height="320">
            
            `,



            <h3>
              Raw Audio Signal
            </h3>

            <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/audio.png" height="120">

            <h3>
              Spectogram showing energy located in frequency bins over time intervals 
            </h3>
            <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/screenshot.png" width="740" height="350">
            
            
            <h2> Methods </h2>
            
            I attempt to reproduce the neural network archticture described by Manuel Minguez Carretero in his thesis. He proposes several neural network architectures for solving this problem, which he trained on the MusicNet database, an MIR dataset of piano recordings and sheet music.  In this project I instead train models using the GuitarSet & the Maestro datasets for performing guitar and piano transcription.
            
            <h3>
              Network Architecture
            </h3>
            <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/cnn.png" width="560" height="320">
            
            <h3>
              Data Preprocessing

            </h3>

            <p>
            In order to normalize the data, the mean value (for each frequency bin of the spectogram) taken over all of the training data must be calculated.
            Since the data is too large to fit into memory, I implemented an algorithm known as Welford's algorithm, an iterative algorithm which calculates the running mean of a dataset such that not all of the data must be loaded into memory at once.

            </p>
            
            <h3>
              Training the neural network
            </h3>
            
            <p>
            The transforms and processed annotation numpy arrays are saved to S3 from where they are downloaded to an EC2 GPU instance.  The data is fed into a Keras generator (fit generator API) for training the neural network.  

   
            </p>

            <h3>
              Results
            </h3>
            <p>
            As of right now, the neural network was unable to make proper predictions..  I'm not entirely sure where I've gone wrong.
            </p>
