import tensorflow as tf

def create_tf_dataset(input, label):
    # Read the image binary data
    image = open(input, 'rb').read()

    # Encode the label as bytes
    label_bytes = label.encode('utf-8')

    # Create a feature dictionary
    feature = {
        'input': tf.train.Feature(bytes_list=tf.train.BytesList(value=[input])),
        'label': tf.train.Feature(bytes_list=tf.train.BytesList(value=[label_bytes])),
    }

    # Create a TensorFlow Example object
    tf_data = tf.train.Example(features=tf.train.Features(feature=feature))
    return tf_data


# Example usage
tf_record_filename = 'DataForTF'

#read the csv file to get the input paths and label
import csv

data = csv.reader(open('file name'))


with tf.io.TFRecordWriter(tf_record_filename) as writer:
    for row in data:
        tf_example = create_tf_dataset(row[0], row[1])
        writer.write(tf_example.SerializeToString())



