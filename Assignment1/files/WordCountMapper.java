import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;


/*****
        Word Counter Mapper class. 
*****/
public class WordCountMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable>
{
    //Hadoop supported data types
    private final static IntWritable one = new IntWritable(1);
    private                    Text word = new Text();

    
    /*****
        Map method that performs the tokenizer job and framing the initial key value pairs
    ***/
    public void map(LongWritable key, 
                    Text value, 
                    OutputCollector<Text, IntWritable> output, 
                    Reporter reporter) 
    throws IOException
    {
        /***
            taking one line at a time and tokenizing the same
        */
        String line = value.toString();
        StringTokenizer tokenizer = new StringTokenizer(line);
        
        /***
            iterating through all the words available in that line and forming the key value pair
            as (word, 1).
            Notice that the 1 is actually a writable Int special type for mapreduce
        */
        while (tokenizer.hasMoreTokens())   {

            word.set(tokenizer.nextToken());    //Word is the map reduce Text type
            output.collect(word, one);          //Send to output collector which inturn passes the same to reducer
        }

    }

}
